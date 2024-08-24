$(document).ready(function() {
    const themeToggle = $('#themeToggle');
    const themeLabel = $('#themeLabel');

    // Load the saved theme from localStorage
    const currentTheme = localStorage.getItem('theme') || 'light';
    if (currentTheme === 'dark') {
        $('body').addClass('dark-mode');
        themeToggle.prop('checked', true);
        themeLabel.text('Dark Mode');
    }

    // Toggle theme on switch change
    themeToggle.change(function() {
        if (this.checked) {
            $('body').addClass('dark-mode');
            themeLabel.text('Dark Mode');
            localStorage.setItem('theme', 'dark');
        } else {
            $('body').removeClass('dark-mode');
            themeLabel.text('Light Mode');
            localStorage.setItem('theme', 'light');
        }
    });

    $('#movieForm').submit(function(event) {
        event.preventDefault();
        
        const movieTitle = $('#movieTitle').val();
        $('#results').html('Loading...');

        $.ajax({
            url: '/scrape',
            method: 'GET',
            data: { title: movieTitle },
            success: function(response) {
                const imdbUrl = `https://www.imdb.com/title/${response.imdbID}/`;

                let resultHtml = `
                    <div class="movie-details">
                        <a href="${imdbUrl}" target="_blank">
                            <img src="${response.poster_url}" alt="${response.title} poster" class="movie-poster">
                        </a>
                        <div class="movie-info">
                            <h2>${response.title} (${response.year})</h2>
                            <p><strong>IMDb ID:</strong> ${response.imdbID}</p>
                            <p><strong>Plot Summary:</strong> ${response.plot_summary}</p>
                            <p><strong>Rating:</strong> ${response.rating}</p>
                            <p><strong>Runtime:</strong> ${response.runtime}</p>
                            <p><strong>Age Restriction:</strong> ${response.age_restriction}</p>
                            <p><strong>Awards:</strong> ${response.awards} (${response.awards_total})</p>
                            <p><strong>Directors:</strong> ${response.directors.join(', ')}</p>
                            <p><strong>Actors:</strong> ${response.actors}</p>
                        </div>
                    </div>
                `;
                $('#results').html(resultHtml);
            },
            error: function() {
                $('#results').html('No results found or an error occurred.');
            }
        });
    });
});
