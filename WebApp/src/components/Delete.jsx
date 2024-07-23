import React, {  useState } from 'react';
import axios from 'axios';

function Delete(props){
    const [id, setId] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.delete(`http://127.0.0.1:8000/items/${id}`, {})
          .then(function (response) {
            setId("");
            // alert("Data entry deleted\n{\nItem_name: "+ 
            //     response.data[0].item_name+"\nBrand_name: "+
            //     response.data[0].brand_name+"\nPrice: "+
            //     response.data[0].price+"\nID: "+
            //     response.data[0].id+ "\n}"); 
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
    return (<div>
        <form onSubmit={handleSubmit}>
            <label>DELETE</label>
                <input type='number' value={id} placeholder='Enter ID of item to be Deleted' onChange={(e) => setId(e.target.value)} />
            <button type='submit'>Delete</button>
        </form>
    </div>)
}

export default Delete;