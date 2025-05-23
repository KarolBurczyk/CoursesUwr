import type { Todo, Action } from './types';

interface Props {
  todo: Todo;
  dispatch: React.Dispatch<Action>;
  isFirst: boolean;
  isLast: boolean;
}

const TodoItem = ({ todo, dispatch, isFirst, isLast }: Props) => (
  <li
    className={`todo__container ${todo.completed ? 'todo__container--completed' : ''}`}
  >
    <span className="todo-element todo-name">{todo.text}</span>
    <button
      className="todo-element todo-button"
      onClick={() => dispatch({ type: 'TOGGLE', payload: todo.id })}
    >
      ✓
    </button>
    <button
      className="todo-element todo-button"
      onClick={() => dispatch({ type: 'REMOVE', payload: todo.id })}
    >
      🗑
    </button>
    {!isFirst && (
      <button
        className="todo-element todo-button move-up"
        onClick={() => dispatch({ type: 'MOVE_UP', payload: todo.id })}
      >
        ↑
      </button>
    )}
    {!isLast && (
      <button
        className="todo-element todo-button move-down"
        onClick={() => dispatch({ type: 'MOVE_DOWN', payload: todo.id })}
      >
        ↓
      </button>
    )}
  </li>
);

export default TodoItem;
