import React, { useState, useEffect } from 'react';
import FilmSelect from '../components/FilmSelect';
import FilmDetail from '../components/FilmDetail';


const GhibliContainer = () => {
    const [film, setFilm] = useState([]);
    const [selectedFilm, setSelectedFilm] = useState(null);

    useEffect(() => {
        fetch("https://ghibliapi.herokuapp.com/films")
            .then(res => res.json())
            .then(data => setFilm(data))
    }, []);

    const handleFilmSelect = (url) => {
        fetch(url)
            .then(res => res.json())
            .then(data => setSelectedFilm(data))
    }



    return (
        <>
            <h1 className='App-header'>The Films of Studio Ghibli</h1>
            <div>
                <FilmSelect allFilms={film} onFilmSelect={handleFilmSelect} />
                {selectedFilm ? <FilmDetail film={selectedFilm} /> : null}

            </div>
        </>
    );
}

export default GhibliContainer;