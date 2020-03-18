import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import PrimarySearchAppBar from './searchBar/Bar';

import SingleLineGridList from './messier/messierList';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

class App extends Component {
  token = null;
  state = {
    query: "",
    messier: [],
    error: null,
    isLoad: false
  };
  onChange = e => {
    console.log(e.query)
    const value = e.query;
    this.setState({
      query: value
    });

    this.api(value);
  };
  api = query => {
    const proxyurl = "https://cors-anywhere.herokuapp.com/";
    const url = `https://anh.pythonanywhere.com/api/v2/messier-catalogue/${query}`;
    const token = {};
    this.token = token;

    fetch(proxyurl + url)
      .then(results => results.json())
      .then((dt) => {
        // console.log(dt)
        if (this.token === token) {
          if (dt.hasOwnProperty("message")) {
            this.setState({ 
              isLoad: true,
              messier : [],
              error : dt.message
            })
          } else {
            if (dt.data instanceof Object) {
              this.setState({ 
                isLoad: true,
                messier: [dt.data] 
              });
            } else {
              this.setState({ 
                isLoad: true,
                messier: dt.data 
              });
            }
          }
        }
      }, (error) => {
        this.setState({
          isLoad: true,
          error: error.message  
        })
      })
      // .catch((e) => {console.log(e)});
  };
  render() {
      return (
          <div className="App">
            <PrimarySearchAppBar onChange={this.onChange}/>
            {/* {
              this.state.messier &&
              console.log(this.state.messier)
            } */}
            <SingleLineGridList data={this.state.messier}/>
          </div>
        );
  }
}

export default App;
