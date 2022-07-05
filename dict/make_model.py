 data["rows"] = 10
    data["cols"] = 10
    data["board_size"] = 500 
    data["cell_size"] = data["board_size"]/data["rows"]
    data["ships"] = 5
    data["computer"] = emptyGrid(data["rows"],data["cols"])
    data["user"] = emptyGrid(data["rows"],data["cols"])
    data["computer"] = addShips(data["computer"],data["ships"])
    # data["user"] = addShips(data[computer],data[ships]  
    
    test.testMakeModel()