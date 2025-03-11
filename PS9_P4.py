def get_pay_rate(job_code):
  rates = {'L': 25, 'A': 30, 'J': 50}
  return rates.get(job_code.upper(), 0)  # Default to 0 if invalid job code

def calculate_gross_pay(job_code, hours_worked):
  pay_rate = get_pay_rate(job_code)
  if hours_worked > 40:
      overtime_hours = hours_worked - 40
      gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
  else:
      gross_pay = hours_worked * pay_rate
  return gross_pay

def main():
  total_gross_pay = 0
  while True:
      last_name = input("Enter employee's last name: ")
      if last_name.lower() == 'exit':
          break
      job_code = input("Enter job code (L, A, J): ")
      hours_worked = float(input("Enter hours worked: "))

      gross_pay = calculate_gross_pay(job_code, hours_worked)
      print(f"Employee: {last_name}, Gross Pay: ${gross_pay:.2f}\n")

      total_gross_pay += gross_pay

  print(f"Total Gross Pay for all employees: ${total_gross_pay:.2f}")

if __name__ == "__main__":
  main()
