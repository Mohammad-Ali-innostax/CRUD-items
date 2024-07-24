import React, { useState } from 'react';
import axios from 'axios';

function Create(props){
    const [itemName,setItemName] = useState("");
    const [brandName, setBrandName] = useState("");
    const [price, setPrice] = useState("");


    const handleSubmit = (event) => {
        event.preventDefault();

        var payload = [{
          "item_name":itemName,
          "brand_name": brandName,
          "price": price
        }];
        axios.post(`http://127.0.0.1:8000/items/`, payload)
          .then(function (response) {
            // alert("Database Updated");
            console.log("success");
            setBrandName("");
            setItemName("");
            setPrice("");
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
          <label>CREATE</label>
            <input type='text' value={itemName} placeholder='Enter Item Name' onChange={(e) => setItemName(e.target.value)} />
            <input type='text' value={brandName} placeholder='Enter Brand Name' onChange={(e) => setBrandName(e.target.value)} />
            <input type='number' value={price} placeholder='Enter price' onChange={(e) => setPrice(e.target.value)} />
            <button type='submit'>Submit</button>
        </form>
    </div>)
}

export default Create;