export interface Todo {
  id: number;
  text: string;
  completed: boolean;
}

export type Action =
  | { type: 'ADD'; payload: string }
  | { type: 'REMOVE'; payload: number }
  | { type: 'TOGGLE'; payload: number }
  | { type: 'MOVE_UP'; payload: number }
  | { type: 'MOVE_DOWN'; payload: number }
  | { type: 'CLEAR_ALL' };
