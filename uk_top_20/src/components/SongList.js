import React from "react";
import Song from "./Song";

const SongList = ({ songs }) => {

    const songItems = songs.map((song, index) => {
        return (<div>
            <h2>{index + 1}</h2>
            <Song song={song} position={index} />
            <hr></hr>
        </div>)
    }

    )

    return (
        <div>
            <ul>
                {songItems}
            </ul>
        </div>
    )

}

export default SongList