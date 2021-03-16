<template>
  <div id="app">
    <HelloWorld msg="Weather App" />
    <h1 class="Search by city"></h1>
    <div class="is-size-4">Current temperature and condition</div>
    <input v-model="city" class="input" type="text" placeholder="Search city" />
    <button @click="searchCity(city)" class="button">Search that city!</button>
    <div v-if="success_current">
      <div
        class="is-size-4 temperature"
      >Now showing the temperature in {{city}}, last updated {{time}}</div>
      <table class="table is-bordered">
        <thead>
          <tr>
            <th>Condition</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="key in Object.keys(hide)" :key="key">
            <th>{{key}}</th>
            <th>{{hide[key][0]}} °C</th>
          </tr>
        </tbody>
      </table>
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
      success_current: false,
      time: null,
      feels_like: 0
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
            self.time = response.data["time"];
            self.feels_like = response.data["feels_like"];
          })
          .catch(function(error) {
            alert("Please enter a valid city name");
            console.log(error);
          });
      } else {
        alert("Please enter a city name");
      }
    }
  },
  computed: {
    hide: function() {
      return {
        Temperature: [this.temperature, false],
        Description: [this.description, false],
        "Feels like": [this.feels_like, false]
      };
    }
  }
};
</script>

<style>
.input {
  width: 50%;
  margin-right: 0.5rem;
}
.table {
  margin: 0 auto;
  margin-top: 2rem;
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
