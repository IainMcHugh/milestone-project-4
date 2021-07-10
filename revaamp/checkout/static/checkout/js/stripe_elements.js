const stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
const client_secret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripe_public_key);
const elements = stripe.elements();
const style = {
    base: {
      color: "#32325d",
    }
  };
const card = elements.create('card', { style });
card.mount('#card-element');