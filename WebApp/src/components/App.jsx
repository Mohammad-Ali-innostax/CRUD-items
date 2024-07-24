import React, { useState, useEffect } from "react";
import Read from "./Read"
import Create from "./Create";
import Update from "./Update";
import Delete from "./Delete";
import axios from "axios";

function App() {

  const [database, setDatabase] = useState([]);
  const [deleteList, setDeleteList] = useState([]);

  useEffect(() => {
      axios.get('http://127.0.0.1:8000/items/').then((response) => {
        setDatabase(response.data);
      });
    }, []); 
  return (
    <div className="main-body">
      <div className="bottom">
        <Create setDatabase={setDatabase}/> 
        <Update setDatabase={setDatabase}/>
        <Delete setDatabase={setDatabase} deleteList={deleteList} setDeleteList={setDeleteList}/>
      </div>
      <Read database={database} deleteList={deleteList} setDeleteList={setDeleteList}/>
    </div>
  );
}

export default App;