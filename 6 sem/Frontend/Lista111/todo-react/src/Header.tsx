import type { Todo, Action } from './types';

interface Props {
  todos: Todo[];
  dispatch: React.Dispatch<Action>;
}

const Header = ({ todos, dispatch }: Props) => (
  <header className="todos-header__container">
    <h2>
      Todo List (<span>{todos.filter(todo => !todo.completed).length}</span> remaining)
      <button className="todos-clear" onClick={() => dispatch({ type: 'CLEAR_ALL' })}>
        Clear all
      </button>
    </h2>
  </header>
);

export default Header;
