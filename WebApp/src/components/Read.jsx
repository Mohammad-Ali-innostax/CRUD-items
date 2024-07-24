import React, { useEffect} from "react";

function Read(props) {
    const database = props.database;

    useEffect(()=>{
      props.setDeleteList(props.deleteList); //sending data to deletelist
      // console.log(props.deleteList);
      // eslint-disable-next-line
    },[props.deleteList])

    function handleCheckboxChange(id){
      if(props.deleteList.includes(id)){
        const newIds = props.deleteList.filter((ids) => ids !== id);
        props.setDeleteList( newIds);
      }else{
        props.setDeleteList(oldList => [...oldList,id] );
      }
    }

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
            <div className="table-index">
              <input
                  type="checkbox"
                  checked={props.deleteList.includes(entry.id) || false}
                  onChange={() => handleCheckboxChange(entry.id)}
              />
              {entry.id}
            </div>
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