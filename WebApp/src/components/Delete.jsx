import React from 'react';
import axios from 'axios';

function Delete(props){
    // const [id, setId] = useState("");
    const handleSubmit = (event) => {
        event.preventDefault();
        for ( var a = 0; a<props.deleteList.length;a++){
            axios.delete(`http://127.0.0.1:8000/items/${props.deleteList[a]}`, {})
          .then(function (response) {
            // setId("");
            console.log("success");
            axios.get('http://127.0.0.1:8000/items/').then((response) => {
                props.setDatabase(response.data);
                });
          })
          .catch(function (error) {
            if(error.response.status === 422 || error.response.status === 405){
                alert("Incomplete Data");
            }
            if(error.response.status === 404){
                alert("Data does not exist in the database");
            }
            console.log(error);
          });
        }
        props.setDeleteList([]);
      }    
    return (<div>
        <form onSubmit={handleSubmit}>
            <label>Mark Checkboxes to select the Items to be Deleted</label>
                {/* <input type='number' value={id} placeholder='Enter ID of item to be Deleted' onChange={(e) => setId(e.target.value)} /> */}
            <button type='submit'>Delete</button>
        </form>
    </div>)
}

export default Delete;