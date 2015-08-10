import React from "react";

import styles from "./App.sass";

class App extends React.Component {
  render() {
    return (
      <p className={ styles.title }>
        This is App
      </p>
    );
  }
}

export default App;
