exports.handler = async (event) => {
  const secret = process.env.HOOK_ADMIN_SECRET;
  const reqSecret = event.headers["x-hook-secret"];

  if (reqSecret !== secret) {
    return {
      statusCode: 403,
      body: JSON.stringify({ error: "Unauthorized" }),
    };
  }

  return {
    statusCode: 200,
    body: JSON.stringify({ message: "Valid hook access" }),
  };
};
