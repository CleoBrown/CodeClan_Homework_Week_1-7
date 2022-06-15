import React from "react";

const Song = ({ song }) => {
    return (
        <>
            <h4>
                {song["im:name"]["label"]}
            </h4>
            <p>{song["im:artist"]["label"]}</p>



        </>
    )
}

export default Song;