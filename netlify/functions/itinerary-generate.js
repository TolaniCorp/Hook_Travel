exports.handler = async (event, context) => {
  const data = JSON.parse(event.body || "{}");
  const destination = data.destination || "Unknown";

  const response = {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message: `📍 HOOK Itinerary started for ${destination}`,
      data,
    }),
  };

  return response;
};
