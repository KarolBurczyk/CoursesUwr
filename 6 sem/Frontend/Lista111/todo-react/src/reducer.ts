import type { Todo, Action } from './types';

export const todoReducer = (state: Todo[], action: Action): Todo[] => {
  switch (action.type) {
    case 'ADD':
      return [...state, { id: Date.now(), text: action.payload, completed: false }];
    case 'REMOVE':
      return state.filter(todo => todo.id !== action.payload);
    case 'TOGGLE':
      return state.map(todo =>
        todo.id === action.payload ? { ...todo, completed: !todo.completed } : todo
      );
    case 'MOVE_UP': {
      const idx = state.findIndex(todo => todo.id === action.payload);
      if (idx > 0) {
        const newState = [...state];
        [newState[idx - 1], newState[idx]] = [newState[idx], newState[idx - 1]];
        return newState;
      }
      return state;
    }
    case 'MOVE_DOWN': {
      const idx = state.findIndex(todo => todo.id === action.payload);
      if (idx < state.length - 1) {
        const newState = [...state];
        [newState[idx + 1], newState[idx]] = [newState[idx], newState[idx + 1]];
        return newState;
      }
      return state;
    }
    case 'CLEAR_ALL':
      return [];
    default:
      return state;
  }
};
