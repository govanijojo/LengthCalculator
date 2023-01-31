# Function to convert length from meters to inches, feet
def convert_length(meters):
  inches = meters * 39.37
  feet = meters * 3.281

  return inches, feet

# Input value in meters
meters = float(input("Enter the length in meters: "))

# Call the function and get the converted values in inches and feet
inches, feet = convert_length(meters)
 
# Print the converted values 
print("Length in Inches: %.2f" %inches) 
print("Length in Feet: %.2f" %feet)
