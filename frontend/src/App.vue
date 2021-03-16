<template>
  <div id="app">
    <HelloWorld msg="Weather App" />
    <h1 class="Search by city"></h1>
    <div class="is-size-4">Current temperature and condition</div>
    <input v-model="city" class="input" type="text" placeholder="Search city" />
    <button @click="searchCity(city)" class="button">Search that city!</button>
    <div v-show="success_current">
      <div
        class="is-size-4 temperature"
      >The temperature is {{temperature}} °C in {{city}} and is {{description}}</div>
    </div>
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
    return {
      city: "",
      temperature: 0,
      description: "",
      success_current: false
    };
  },
  methods: {
    searchCity: function() {
      if (this.city.length !== 0) {
        let self = this;
        axios
          .post(`http://127.0.0.1:8000/city/`, {
            city_name: this.city
          })
          .then(function(response) {
            self.success_current = true;
            console.log(response.data);
            self.temperature = response.data["current_temp"];
            console.log(self.temperature);
            self.description = response.data["description"];
            console.log(self.description);
          })
          .catch(function(error) {
            alert("Please enter a valid city name");
            console.log(error);
          });
      } else {
        alert("Please enter a city name");
      }
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
