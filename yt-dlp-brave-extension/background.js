chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (!message) return;

  if (message.type === 'AERODL_OPEN_POPUP') {
    // Opens extension popup/dashboard in a dedicated tab
    chrome.tabs.create({ url: chrome.runtime.getURL('popup.html') });
    sendResponse({ ok: true });
    return;
  }

  if (message.type !== 'AERODL_FETCH') return;

  (async () => {
    try {
      const res = await fetch(message.url, message.options || {});
      const text = await res.text();
      let json = {};
      try {
        json = text ? JSON.parse(text) : {};
      } catch {
        json = { raw: text };
      }

      sendResponse({
        ok: res.ok,
        status: res.status,
        statusText: res.statusText,
        data: json,
      });
    } catch (err) {
      sendResponse({
        ok: false,
        status: 0,
        statusText: 'FETCH_ERROR',
        data: { error: err?.message || 'Fetch failed' },
      });
    }
  })();

  return true;
});
