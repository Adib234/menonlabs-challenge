<template>
  <div id="app">
    <HelloWorld msg="Weather App" />
    <h1 class="Search by city"></h1>
    <input v-model="city" class="input" type="text" placeholder="Search city" />
    <button @click="searchCity(city)" class="button">Search that city!</button>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import axios from "axios";
export default {
  name: "App",
  components: {
    HelloWorld
  },
  data() {
    return { city: "" };
  },
  methods: {
    searchCity: function() {
      axios
        .post(`http://127.0.0.1:8000/city/`, {
          city_name: this.city
        })
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style>
.input {
  width: 50%;
  margin-right: 0.5rem;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
