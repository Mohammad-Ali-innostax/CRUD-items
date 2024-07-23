import React from "react";

function Read(props) {
    const database = props.database;

    return (
      <div className="database-body-main">
        <div className="database-table-heading">
            <div>ID</div>
            <div>Item Name</div>
            <div>Brand Name</div>
            <div>Item Price</div>
          </div>
      <div className="read-body">
        {database.map((entry, index) => (
          <div className="database-table" key={index}>
            <div className="table-index">{entry.id}</div>
            <div className="table-name">{entry.item_name}</div>
            <div className="table-brand">{entry.brand_name}</div>
            <div className="table-price">{entry.price}</div>
          </div>
        ))}
      </div>
      
      </div>
    );
  }
  

export default Read;