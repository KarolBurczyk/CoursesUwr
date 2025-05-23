import type { Todo, Action } from './types';
import TodoItem from './TodoItem';

interface Props {
  todos: Todo[];
  dispatch: React.Dispatch<Action>;
}

const TodoList = ({ todos, dispatch }: Props) => (
  <ul className="todos__list">
    {todos.map((todo, index) => (
      <TodoItem
        key={todo.id}
        todo={todo}
        dispatch={dispatch}
        isFirst={index === 0}
        isLast={index === todos.length - 1}
      />
    ))}
  </ul>
);

export default TodoList;
