import React from 'react'
import './Searchimage.css'
import SearchIcon from '@mui/icons-material/Search';

const Searchimage = () => {
  return (
    <div className="search">
        <img  alt="" src={SearchIcon}/>
        <h1>it was such a good image that no has ever seen it!</h1>
        <ol>
            <h1>My ITems Listms List</h1>
            <li>My ITems List</li>
            <li>My ITems List</li>
            <li>My ITems List</li>
            <li>My ITems List</li>
        </ol>
    </div>

  )
}
export default Searchimage;