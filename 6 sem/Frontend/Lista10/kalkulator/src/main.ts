import { calculate } from './calculator'

const display = document.getElementById('display') as HTMLDivElement
const buttons = document.querySelectorAll('.btn')

let expression = ''

function updateDisplay() {
  display.textContent = expression || '0'
}

buttons.forEach((button) => {
  const value = (button as HTMLButtonElement).dataset.value

  if (value) {
    button.addEventListener('click', () => {
      expression += value === ',' ? '.' : value
      updateDisplay()
    })
  }
})

document.getElementById('clear')?.addEventListener('click', () => {
  expression = ''
  updateDisplay()
})

document.getElementById('delete')?.addEventListener('click', () => {
  expression = expression.slice(0, -1)
  updateDisplay()
})

document.getElementById('equals')?.addEventListener('click', () => {
  expression = calculate(expression)
  updateDisplay()
})
