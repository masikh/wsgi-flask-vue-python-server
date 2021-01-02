<template>
  <div>
    <section>
      <b-field
        label="Passphrase"
        label-position="on-border">
        <b-input
          v-model="password"
          maxlength="40"
          type="input"/>
      </b-field>

      <b-field
        label="Your text"
        label-position="on-border">
        <b-input
          v-model="text"
          maxlength="4000"
          type="textarea"/>
      </b-field>

      <hr>

      <div class="cipher-decipher">
        <div>
          <b-button
            native-type="submit"
            type="is-primary"
            @click="Cipher">
            Cipher
          </b-button>
        </div>
        <div>
          <b-button
            @click="Decipher">
            Decipher
          </b-button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

export default {
  data () {
    return {
      text: '',
      password: ''
    }
  },
  computed: {},
  created () {},
  methods: {
    Decipher: function () {
      let params = { 'password': this.password, 'text': this.text }
      this.$http.post('/decipher', params)
        .then(response => {
          if (response.data.error) {
            this.errorMessage = response.data.error
          } else {
            this.text = response.data
          }
        })
        .catch(error => {
          this.errorMessage = error.data.message
        })
    },
    Cipher: function () {
      let params = { 'password': this.password, 'text': this.text }
      this.$http.post('/cipher', params)
        .then(response => {
          if (response.data.error) {
            this.errorMessage = response.data.error
          } else {
            this.text = response.data
          }
        })
        .catch(error => {
          this.errorMessage = error.data.message
        })
    }
  }
}
</script>

<style>
section {
  margin-top: 25px;
}

.cipher-decipher {
    display: flex;
    justify-content: center;
}

.cipher-decipher > * {
    margin: 5px;
}
</style>
