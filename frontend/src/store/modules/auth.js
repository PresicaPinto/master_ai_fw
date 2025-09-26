const state = {
  isAuthenticated: false,
  user: null,
  token: null,
};

const mutations = {
  SET_AUTHENTICATED(state, status) {
    state.isAuthenticated = status;
  },
  SET_USER(state, user) {
    state.user = user;
  },
  SET_TOKEN(state, token) {
    state.token = token;
  },
};

const actions = {
  login({ commit }, { email, password }) {
    // Simulate API call
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (email === 'test@example.com' && password === 'password') {
          const user = { id: 1, email: 'test@example.com' };
          const token = 'fake-jwt-token';
          commit('SET_AUTHENTICATED', true);
          commit('SET_USER', user);
          commit('SET_TOKEN', token);
          resolve(user);
        } else {
          reject(new Error('Invalid credentials'));
        }
      }, 1000);
    });
  },
  logout({ commit }) {
    commit('SET_AUTHENTICATED', false);
    commit('SET_USER', null);
    commit('SET_TOKEN', null);
  },
};

const getters = {
  isAuthenticated: (state) => state.isAuthenticated,
  currentUser: (state) => state.user,
  authToken: (state) => state.token,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
