import { evaluate } from 'mathjs'

export function calculate(expression: string): string {
    try {
        const replacedExpr = expression.replace(/,/g, '.')
        const result = evaluate(replacedExpr)
        return result.toString()
    } catch {
        return 'Error'
    }
}
