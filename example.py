from gridapi import GridApi


if __name__ == '__main__':
    
    grid = GridApi("http://localhost:4444")

    print(grid.get_status())

