import './App.css';
import React, { useState } from 'react';

function App() {

  const [items, setItems] = useState([
    { name: "repot acer tree" },
    { name: "repot holly tree" },
    { name: "cut grass" },
    { name: "remove dandelions" },
    { name: "chase key cutting" },
    { name: "revise show and tell" },
  ]);

  const [newItem, setNewItem] = useState("");

  const itemNodes = items.map((item, index) => {
    return (
      <li key={index}><span>{item.name}</span></li>
    )
  })

  const handleItemInput = (event) => {
    setNewItem(event.target.value)
  }

  const saveNewItem = (event) => {
    event.preventDefault();
    const copyItems = [...items]
    copyItems.push({ name: newItem })
    setItems(copyItems)
    setNewItem("")
  }


  return (
    <div className="App">
      <h1>To Do's</h1>

      <form onSubmit={saveNewItem}>
        <label htmlFor="new-item">Add new item:</label>
        <input id="new-item" type="text" value={newItem} onChange={handleItemInput} />
        <input type="submit" value="Save item" />
      </form>

      <ul>
        {itemNodes}
      </ul>

    </div>
  );
}

export default App;
