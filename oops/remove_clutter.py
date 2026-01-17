# rename all clutter things
import os 
print("wellcome to fix clutter \n")
path = "/Users/misss/OneDrive/Pictures/Screenshots" # chnage path according your need

class fix:
    print(" clutting start .....")
    def __init__(self, user):
            self.user = user
    def clut(self):
          if self.user == 1:
            files = os.listdir(path)
            i = 1
            for file in files:
                if file.endswith(".png"): # chnage extension a/c to you
                # 1. Purana Pata (Folder + / + PuranaNaam)
                    my_source = f"{path}/{file}"

                        # 2. Naya Pata (Folder + / + Number + .png)
                    my_dest = f"{path}/{i}.png"

                        # 3. Action
                    os.rename(my_source, my_dest)

                        # 4. Next number ki tayari
                    i = i + 1
                    print(f"Renamed {file} to {i-1}.png") # Ye line bas dekhne ke liye hai

data = int(input("enter 1  or 2 :"))
clutter = fix( data )
print(clutter.clut())
print("done")
                
            
                
                                