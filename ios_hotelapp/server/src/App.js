import React, { Component, PropTypes } from 'react';
import './App.css';
import { messageSenders } from "./jsAPI";

class App extends Component {
  render() {
    return (
      <div className="App">
        {!this.props.search && (
          <div className="App-notready">Page is not ready yet</div>
        )}
        {this.props.search && !this.props.results && (
          <div className="App-loadingsearch">Loading search results...</div>
        )}
        {this.props.search && this.props.results && (
          <ul className="App-searchresults">
            {this.props.results.map((result, i) => {
              return (
                <li key={i} onClick={messageSenders.HOTEL_API_HOTEL_SELECTED.bind(this, result)}>
                  <img src={result.hotel.imageURL} alt={`${result.hotel.name} thumbnail`} />
                  <div className="App-searchresults-description">
                    {result.hotel.name}
                  </div>
                  <div className="App-searchresults-price">
                    ${result.price}
                  </div>
                </li>
              );
            })}
          </ul>
        )}
      </div>
    );
  }
}
App.propTypes = {
  search: PropTypes.object,
  results: PropTypes.array,
}

export default App;
