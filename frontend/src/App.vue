<template>
  <div id="app">
    <HelloWorld msg="Weather App" />
    <h1 class="Search by city"></h1>
    <div class="is-size-4">Current temperature and condition</div>
    <input v-model="current_city" class="input" type="text" placeholder="Search city" />
    <button @click="searchCity()" class="button">Search that city!</button>
    <div v-if="success_current">
      <div
        class="is-size-4 temperature"
      >Now showing the temperature in {{current_city}}, last updated {{time}}</div>
      <div class="all-tags">
        <div class="checkbox" v-for="(key,index) in Object.keys(hide)" :key="key">
          <label class="checkbox">
            <input @change="deleteTag(index)" type="checkbox" />
            {{key}}
          </label>
        </div>
      </div>
      <table class="table is-bordered">
        <thead>
          <tr>
            <th>Condition</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(key,index) in Object.keys(hide)" :key="key">
            <th v-if="!shown[index]">{{key}}</th>
            <th v-if="!shown[index]">{{hide[key]}}</th>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="is-size-4">Temperature forecasts</div>
    <input v-model="forecasts_city" class="input" type="text" placeholder="Search city" />
    <button @click="createGraph()" class="button">Search that city!</button>
    <img v-if="success_forecast" :src="image" />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import axios from "axios";
//import Chart from "chart.js";

export default {
  name: "App",
  components: {
    HelloWorld
  },
  data() {
    return {
      current_city: "",
      forecasts_city: "",
      temperature: 0,
      description: "",
      success_current: false,
      success_forecast: false,
      time: null,
      feels_like: 0,
      min_temp: 0,
      max_temp: 0,
      humidity: 0,
      pressure: 0,
      shown: [false, false, false, false, false, false, false],
      image: ""
    };
  },
  methods: {
    searchCity: function() {
      if (this.current_city.length !== 0) {
        let self = this;
        axios
          .post(`http://127.0.0.1:8000/city/`, {
            city_name: this.current_city
          })
          .then(function(response) {
            self.success_current = true;
            console.log(response.data);
            self.temperature = response.data["current_temp"];
            self.temperature += " °C";
            console.log(self.temperature);
            self.description = response.data["description"];
            self.time = response.data["time"];
            self.feels_like = response.data["feels_like"];
            self.feels_like += " °C";
            self.min_temp = response.data["min_temp"];
            self.min_temp += " °C";
            self.max_temp = response.data["max_temp"];
            self.max_temp += " °C";
            self.humidity = response.data["humidity"];
            self.pressure = response.data["Pressure"];
          })
          .catch(function(error) {
            alert("Please enter a valid city name");
            console.log(error);
          });
      } else {
        alert("Please enter a city name");
      }
    },
    deleteTag: function(tag) {
      this.$set(this.shown, tag, !this.shown[tag]);
      console.log(this.shown[tag]);
    },
    createGraph: function() {
      if (this.forecasts_city.length !== 0) {
        let self = this;
        axios
          .post(`http://127.0.0.1:8000/forecast/`, {
            city_name: this.forecasts_city
          })
          .then(function(response) {
            console.log(response.data);
            self.success_forecast = true;
            self.image = "data:image/png;base64, " + response.data;
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
        Temperature: this.temperature,
        Description: this.description,
        "Feels like": this.feels_like,
        "Minimum Temperature": this.min_temp,
        "Maximum temperature": this.max_temp,
        Humidity: this.humidity,
        Pressure: this.pressure
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
.has-addons {
  margin-left: 0.5rem;
}
.all-tags {
  margin: 0 auto;
  width: 50%;
  align-items: center;
  display: flex;
}
.checkbox {
  margin-left: 0.5rem;
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
