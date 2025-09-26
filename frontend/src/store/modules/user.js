const state = {
  profile: null,
};

const mutations = {
  SET_USER_PROFILE(state, profile) {
    state.profile = profile;
  },
};

const actions = {
  fetchUserProfile({ commit }, userId) {
    // Simulate API call
    return new Promise((resolve) => {
      setTimeout(() => {
        const profile = { id: userId, name: 'John Doe', bio: 'A test user.' };
        commit('SET_USER_PROFILE', profile);
        resolve(profile);
      }, 500);
    });
  },
};

const getters = {
  userProfile: (state) => state.profile,
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
};
