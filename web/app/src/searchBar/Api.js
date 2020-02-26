import React, {Component} from 'react';
import InputBase from '@material-ui/core/InputBase';
import SingleLineGridList from '../messier/messierList';

class Search extends Component {
    // constructor(props) {
    //   super(props)
    // }
    token = null;
    state = {
      query: "",
      messier: []
    };
    onChange = e => {
      const { value } = e.target;
      this.setState({
        query: value
      });
  
      this.search(value);
    };
  
    search = query => {
      const proxyurl = "https://cors-anywhere.herokuapp.com/";
      const url = `https://anh.pythonanywhere.com/api/v2/messier-catalogue/${query}`;
      const token = {};
      this.token = token;
  
      fetch(proxyurl + url)
        .then(results => results.json())
        .then(dt => {
          if (this.token === token) {
              console.log(dt)
            this.setState({ messier: dt.data });
          }
        }).catch((e) => {console.log(e)});
    };
  
    componentDidMount() {
      this.setState({
        classes: this.props
      });
      console.log(this.props);
      this.search("");
    }
  
    render() {
      const { classes } = this.props;
      return (
        // <form>
        //   <input
        //     type="text"
        //     className="search-box"
        //     placeholder="Search for..."
        //     onChange={this.onChange}
        //   />
        //   {this.state.messier.map(mes => (
        //     <ul key={mes.id}>
        //       <li>{mes.id}</li>
        //     </ul>
        //   ))}
        // </form>
        <InputBase
          placeholder="Search…"
          // onChange={handleInputSearchOnChange}
          classes={{
            root: {color: 'inherit'},
            input: classes.inputInput,
          }}
          inputProps={{ 'aria-label': 'search' }}
          onChange={this.onChange}
        />
      );
    }
  }

  export default Search;