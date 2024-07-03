def perform_operation(num1, num2, operation):
  match(operation):
    case 'add':
      return num1 + num2
    case 'subtract':
      return num1 - num2
    case 'multiply':
      return num1 * num2
    case 'divide':
      if num2 == 0:
        return "Undefined"
      else:
        return num1 / num2
    case _:
      return "Sorry this operation is not supported \nEnter one of the four operations" 