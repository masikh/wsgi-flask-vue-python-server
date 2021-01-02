<template>
  <section>
    <div
      class="card container"
      @submit="login">
      <img
        alt="Logo"
        class="logo"
        src="@/assets/ankh.png"
      >
      <form>
        <b-field
          :type="message ? 'is-danger' : 'is-primary'">
          <b-input
            v-model="username"
            placeholder="username"
            required/>
        </b-field>
        <b-field
          :message="message"
          :type="message ? 'is-danger' : 'is-primary'">
          <b-input
            v-model="password"
            password-reveal
            required
            placeholder="Password"
            type="password"/>
        </b-field>
        <b-button
          native-type="submit"
          type="is-primary">
          <b-icon
            icon="sign-in-alt"
            pack="fas"/>
          <span>Login</span>
        </b-button>
      </form>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: '',
      message: ''
    }
  },
  methods: {
    login: function () {
      let data = {
        username: this.username,
        password: this.password
      }
      this.$http.post('login', data)
        .then(response => {
          if (response.data.error) {
            this.message = JSON.stringify(response.data.error)
            return
          }
          this.$http.defaults.headers.common['Authorization'] = response.data.token
          this.$store.commit('login', { token: response.data.token, username: data.username })
          this.$router.push('/')
        })
        .catch(error => {
          this.message = error.data.message || JSON.stringify(error)
        })
    }
  }
}
</script>

<style scoped>
.card {
  max-width: 500px;
  padding: 20px;
}

.logo {
  width: 150px;
}
</style>
