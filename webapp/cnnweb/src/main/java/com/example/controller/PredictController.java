package com.example.controller;

import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.*;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

@Controller
public class PredictController {

    private static final String ML_URL = "http://127.0.0.1:8000/predict";

    @GetMapping("/")
    public String uploadPage() {
        return "upload"; // viser hovedsiden hvor man ser modellgraf og har muligheten til å uploade bilde
    }

    @PostMapping("/predict")
    public String predict(@RequestParam("file") MultipartFile file, Model model) {
        if (file == null || file.isEmpty()) {
            model.addAttribute("message", "Velg et bilde før du klassifiserer.");
            return "upload";
        }
        try {
            // Bygg multipart Body -> Python-API
            MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();
            ByteArrayResource res = new ByteArrayResource(file.getBytes()) {
                @Override public String getFilename() { return file.getOriginalFilename(); }
            };
            body.add("file", res);

            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.MULTIPART_FORM_DATA);

            RestTemplate rest = new RestTemplate();
            ResponseEntity<String> resp =
                rest.postForEntity(ML_URL, new HttpEntity<>(body, headers), String.class);

            // Minimal parsing uten ekstra libs
            String json = resp.getBody(); // {"label":"hockey","prob":0.9635}
            String label = json.replaceAll(".*\"label\"\\s*:\\s*\"([^\"]+)\".*", "$1");
            String probStr = json.replaceAll(".*\"prob\"\\s*:\\s*([0-9.]+).*", "$1");
            double prob = 0.0;
            try { prob = Double.parseDouble(probStr); } catch (Exception ignored) {}
            int pct = (int)Math.round(prob * 100.0);

            model.addAttribute("message", "Du lastet opp et bilde av " + label + " (" + pct + "%).");
        } catch (Exception e) {
            model.addAttribute("message", "Feil: " + e.getMessage());
        }
        return "upload";
    }
}
