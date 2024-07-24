import React, { useState } from 'react';
import axios from 'axios';

function Update(props){
    const [itemName,setItemName] = useState("");
    const [brandName, setBrandName] = useState("");
    const [price, setPrice] = useState("");
    const [id, setId] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();

        var payload = [{
            "item_name":itemName,
            "brand_name": brandName,
            "price": price
        }];
        axios.put(`http://127.0.0.1:8000/items/${id}`, payload)
          .then(function (response) {
            // alert("Database Updated");
            setBrandName("");
            setItemName("");
            setPrice("");
            setId("");
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
            <label>UPDATE</label>
                <input type='number' value={id} placeholder="Enter ID of the existing Item" onChange={(e) => setId(e.target.value)} />
                <input type='text' value={itemName} placeholder='Enter new Item Name' onChange={(e) => setItemName(e.target.value)} />
                <input type='text' value={brandName} placeholder='Enter new Brand Name' onChange={(e) => setBrandName(e.target.value)} />
                <input type='number' value={price} placeholder='Enter new price' onChange={(e) => setPrice(e.target.value)} />
            <button type='submit'>Submit</button>
        </form>
    </div>)
}

export default Update;