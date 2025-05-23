import { useState } from 'react';
import type { Action } from './types';

interface Props {
  dispatch: React.Dispatch<Action>;
}

const TodoForm = ({ dispatch }: Props) => {
  const [text, setText] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (text.trim()) {
      dispatch({ type: 'ADD', payload: text });
      setText('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="add-item__container">
      <input
        type="text"
        value={text}
        onChange={e => setText(e.target.value)}
        className="add-item__element add-item__input"
        placeholder="What's on your mind?"
        required
      />
      <button type="submit" className="add-item__element add-item__submit">
        Add
      </button>
    </form>
  );
};

export default TodoForm;
