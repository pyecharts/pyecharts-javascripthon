function renderItem(params, api) {
    var coord, size, values;
    values = [api.value(0), api.value(1)];
    coord = api.coord(values);
    size = api.size([1, 1], values);
    return {"type": "sector", "shape": {"cx": params["coordSys"]["cx"], "startAngle": (coord[3] - (size[1] / 2))}};
}

//# sourceMappingURL=tmp.js.map
