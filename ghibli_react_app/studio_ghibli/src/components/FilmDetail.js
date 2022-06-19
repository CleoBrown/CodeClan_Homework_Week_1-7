import React from 'react';


const FilmDetail = ({ film }) => {
    return (

        <>
            <h2>{film.title}</h2>
            <h3>{film.original_title}</h3>
            <img src={film.image} alt={film.title} />
            <p>Directed by: {film.director}</p>
            <p>Release date:{film.release_date}</p>
            <p>Running time: {film.running_time}</p>
            <p></p>
            <p>{film.description}</p>



        </>
    )
}

export default FilmDetail;