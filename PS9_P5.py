def compute_tuition(credit_hours, district_code):
  rates = {'I': 250, 'O': 550}
  return credit_hours * rates.get(district_code.upper(), 0)  # Default to 0 if invalid code

def main():
  total_tuition = 0
  while True:
      last_name = input("Enter student's last name: ")
      if last_name.lower() == 'exit':
          break
      credit_hours = float(input("Enter credit hours: "))
      district_code = input("Enter district code (I for In-district, O for Out-of-district): ")

      tuition_owed = compute_tuition(credit_hours, district_code)
      print(f"Student: {last_name}, Tuition Owed: ${tuition_owed:.2f}\n")

      total_tuition += tuition_owed

  print(f"Total Tuition Owed for all students: ${total_tuition:.2f}")

if __name__ == "__main__":
  main()
