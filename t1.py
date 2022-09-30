from os import name


ctr = 0
excel_filename = "12.csv"
yaml_filename = excel_filename.replace('csv', 'yml')
states = {}
b = []




with open(excel_filename, "r") as excel_csv:
    for line in excel_csv:
        if ctr == 0:
            ctr+=1  # Skip the coumn header
        else:
            # save the csv as a dictionary
            state,dist,tal,vil, name = line.replace(' ','').strip().split(',')
           
             
            b.append({'stateCode':state,'distCode': dist, 'talCode': tal, 'vilCode': vil, 'name':name})

            


with open(yaml_filename, "w+") as yf :
    flag = True
    distCode = 0
    talCode = 0
    yf.write("State: \n")
    for state in b:
        if(flag):
            yf.write("  Code: "+state['stateCode']+"\n")
            yf.write("  LGDCode: "+state['stateCode']+"\n")
            yf.write("  Name: "+state['name']+"\n")
            yf.write("District: \n\n")
            flag = False
        else:
            
            if(distCode != int(state['distCode'])):
                distCode = int(state['distCode'])
                yf.write("  -\n")
                yf.write("     Code: "+state['distCode']+"\n")
                yf.write("     LGDCode: "+state['distCode']+"\n")
                yf.write("     Name: "+state['name']+"\n")
                yf.write("     Taluk: \n\n")
            else:
                if(talCode != int(state['talCode'])):
                    talCode = int(state['talCode'])
                    yf.write("      -\n")
                    yf.write("        Code: "+state['talCode']+"\n")
                    yf.write("        LGDCode: "+state['talCode']+"\n")
                    yf.write("        Name: "+state['name']+"\n")
                    yf.write("        Village: \n\n")
                else:
                    yf.write("          -\n")
                    yf.write("            Code: "+state['vilCode']+"\n")
                    yf.write("            LGDCode: "+state['vilCode']+"\n")
                    yf.write("            Name: "+state['name']+"\n\n")

                    
                
            
                
            
            
        
            
        
            
                
                
            