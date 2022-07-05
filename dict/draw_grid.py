def drawGrid(data, canvas, grid, showShips):
    for i in range(data["rows"]):
        for j in range(data["cols"]):
            if grid[i][j] == SHIP_UNCLICKED:
                #if showShips == True:
                canvas.create_rectangle(j*data["cell_size"], i*data["cell_size"], (j+1)*data["cell_size"], (i+1)*data["cell_size"], fill="yellow")
                #else:
                 #   canvas.create_rectangle(i*data["cell_size"], j*data["cell_size"], (i+1)*data["cell_size"], (j+1)*data["cell_size"], fill="blue")
            else:
                canvas.create_rectangle(j*data["cell_size"], i*data["cell_size"], (j+1)*data["cell_size"], (i+1)*data["cell_size"], fill="blue")

                        
      #      elif grid[i][j] == SHIP_CLICKED:
       #         canvas.create_rectangle(i*data["cell_size"], j*data["cell_size"], (i+1)*data["cell_size"], (j+1)*data["cell_size"], fill="red")
      #      elif grid[i][j] == EMPTY_CLICKED:
      #          canvas.create_rectangle(i*data["cell_size"], j*data["cell_size"], (i+1)*data["cell_size"], (j+1)*data["cell_size"], fill="white")

     #       else:
     #           canvas.create_rectangle(i*data["cell_size"], j*data["cell_size"], (i+1)*data["cell_size"], (j+1)*data["cell_size"], fill="blue")
            
      
    return
       
