from pathlib import Path


SEMI_COLON_SEPARATOR = ";"

def write_to_csv(
    file_path: str, 
    lines: tuple[tuple], 
    header: tuple = (), 
    column_separator: str = SEMI_COLON_SEPARATOR
 ) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path.absolute(), 'w') as file:
        if len(header) > 0:
            file.write(f"{column_separator.join(header)}\n")
        for line in lines:
            file.write(f"{column_separator.join(line)}\n")