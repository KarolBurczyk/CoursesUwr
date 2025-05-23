import { useReducer } from 'react';
import { todoReducer } from './reducer';
import Header from './Header';
import TodoForm from './TodoForm';
import TodoList from './TodoList';

const App = () => {
  const [todos, dispatch] = useReducer(todoReducer, []);

  return (
    <div className="body__wrapper">
      <header className="header__wrapper">
        <h1>Hello, Karol!</h1>
      </header>
      <main className="main">
        <section>
          <TodoForm dispatch={dispatch} />
        </section>
        <section className="todos__container">
          <Header todos={todos} dispatch={dispatch} />
          <TodoList todos={todos} dispatch={dispatch} />
        </section>
      </main>
    </div>
  );
};

export default App;
