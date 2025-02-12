import click
from pathlib import Path
from rich.console import Console
from rich.progress import track
from typing import List, Optional
import fnmatch

console = Console()

def find_files(directory: Path, patterns: List[str], exclude_patterns: List[str]) -> List[Path]:
    """Find all files matching the patterns and not matching exclude patterns."""
    files = []
    for pattern in patterns:
        for path in directory.rglob("*"):
            if path.is_file() and fnmatch.fnmatch(path.name, pattern):
                # Check if file should be excluded
                if not any(fnmatch.fnmatch(str(path.relative_to(directory)), exc) for exc in exclude_patterns):
                    files.append(path)
    return sorted(files)

@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path))
@click.option('--patterns', '-p', default='*.py', 
              help='Comma-separated file patterns to include (e.g., "*.py, *.js")')
@click.option('--exclude', '-e', default='.*, __pycache__/*',
              help='Comma-separated patterns to exclude (e.g., "__pycache__/*, node_modules/*")')
@click.option('--output', '-o', type=click.Path(path_type=Path), 
              default=Path('llm-context-files.txt'),
              help='Output file path')
@click.option('--header', '-h', help='Optional header text for the output file')
@click.option('--language/--no-language', default=True,
              help='Include language hints in code blocks')
def main(directory: Path, patterns: str, exclude: str, 
         output: Path, header: Optional[str], language: bool):
    """Combine multiple files into a single file formatted for LLM context."""
    
    try:
        # Split comma-separated patterns and strip spaces
        pattern_list = [p.strip() for p in patterns.split(',')]
        exclude_list = [e.strip() for e in exclude.split(',')]

        # Load .gitignore patterns from all directories and combine with provided excludes
        all_excludes = exclude_list

        # Find all matching files
        files = find_files(directory, pattern_list, all_excludes)
        
        if not files:
            console.print("[red]No matching files found![/red]")
            return
        
        # Create output file
        with output.open('w', encoding='utf-8') as out:
            # Write header if provided
            if header:
                out.write(f"{header}\n\n")
            
            # Process each file
            for file in track(files, description="Processing files"):
                try:
                    # Write file path as heading
                    relative_path = file.relative_to(directory)
                    out.write(f"File: {relative_path}\n")
                    
                    # Start code block
                    if language:
                        # Guess language from file extension
                        ext = file.suffix.lstrip('.')
                        out.write(f"```{ext}\n")
                    else:
                        out.write("```\n")
                    
                    # Write file contents
                    out.write(file.read_text(encoding='utf-8'))
                    
                    # End code block and add spacing
                    out.write("\n```\n\n")
                    
                except Exception as e:
                    console.print(f"[red]Error processing {file}: {str(e)}[/red]")
        
        console.print(f"[green]Successfully created {output}![/green]")
        console.print(f"Combined {len(files)} files into {output}")
        
    except Exception as e:
        console.print(f"[red]An error occurred: {str(e)}[/red]")
        raise click.Abort()

if __name__ == '__main__':
    main()