import re

pattern = "\d{10}"
with open("service.txt", 'r') as f:
    with open("phonenumbers.txt","w")as f2:
        

        for l in f:
            ls = l.split()
            for w in ls:
                res = re.findall(pattern, w)
                

                if len(res)>0 :
                
                    f2.write(str(res)+"\n")




                    
            

    
